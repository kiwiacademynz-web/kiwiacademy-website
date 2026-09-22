/* ==========================================================
   KIWI NURSE ACADEMY — shared site behaviour
   ========================================================== */
(function () {
  "use strict";
  var C = window.KNA || {};

  /* ---- wire up every data-wa / data-tel / data-email link ---- */
  function wireContactLinks() {
    var waMsg = "Kia ora! I'd like to know more about Kiwi Nurse Academy's IQN, OSCE and OET training.";
    document.querySelectorAll("[data-wa]").forEach(function (el) {
      var msg = el.getAttribute("data-wa-msg") || waMsg;
      el.href = "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(msg);
      if (el.target === undefined || !el.hasAttribute("target")) el.target = "_blank";
      el.rel = "noopener";
    });
    document.querySelectorAll("[data-tel]").forEach(function (el) {
      el.href = "tel:" + C.phone;
      if (el.hasAttribute("data-tel-text")) el.textContent = C.phoneDisplay;
    });
    document.querySelectorAll("[data-email]").forEach(function (el) {
      el.href = "mailto:" + C.email;
      if (el.hasAttribute("data-email-text")) el.textContent = C.email;
    });
    document.querySelectorAll("[data-social]").forEach(function (el) {
      var key = el.getAttribute("data-social");
      if (C.social && C.social[key]) el.href = C.social[key];
    });
    document.querySelectorAll("[data-hours]").forEach(function (el) { el.textContent = C.hours; });
    document.querySelectorAll("[data-addr-india]").forEach(function (el) { el.textContent = C.addressIndia; });
    document.querySelectorAll("[data-addr-nz]").forEach(function (el) { el.textContent = C.addressNZ; });
  }

  /* ---- mobile nav ---- */
  function wireNav() {
    var header = document.querySelector(".site-header");
    var toggle = document.querySelector(".nav-toggle");
    if (!header || !toggle) return;
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("nav-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    /* dropdown (desktop hover/click, mobile click) */
    document.querySelectorAll(".has-sub > .nav__btn").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var parent = btn.closest(".has-sub");
        var willOpen = !parent.classList.contains("is-open");
        document.querySelectorAll(".has-sub.is-open").forEach(function (o) { if (o !== parent) o.classList.remove("is-open"); });
        parent.classList.toggle("is-open", willOpen);
        btn.setAttribute("aria-expanded", willOpen ? "true" : "false");
      });
    });
    document.addEventListener("click", function (e) {
      if (!e.target.closest(".has-sub")) {
        document.querySelectorAll(".has-sub.is-open").forEach(function (o) {
          o.classList.remove("is-open");
          var b = o.querySelector(".nav__btn");
          if (b) b.setAttribute("aria-expanded", "false");
        });
      }
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        header.classList.remove("nav-open");
        toggle.setAttribute("aria-expanded", "false");
        document.querySelectorAll(".has-sub.is-open").forEach(function (o) { o.classList.remove("is-open"); });
      }
    });
  }

  /* ---- pathway chooser (home page) ---- */
  function wireChooser() {
    var root = document.querySelector("[data-chooser]");
    if (!root) return;
    var opts = root.querySelectorAll(".chooser__opt");
    var out = root.querySelector("[data-chooser-out]");
    var answers = JSON.parse(root.getAttribute("data-chooser") || "{}");
    opts.forEach(function (opt) {
      opt.addEventListener("click", function () {
        opts.forEach(function (o) { o.setAttribute("aria-pressed", "false"); });
        opt.setAttribute("aria-pressed", "true");
        var key = opt.getAttribute("data-key");
        var a = answers[key];
        if (a && out) {
          out.innerHTML =
            '<p class="kicker">' + a.kicker + '</p>' +
            '<h3>' + a.title + '</h3>' +
            '<p>' + a.body + '</p>' +
            '<div class="btn-row" style="margin-top:1.1rem">' +
            a.links.map(function (l) { return '<a class="btn btn--kowhai btn--small" href="' + l.href + '">' + l.label + '</a>'; }).join("") +
            '</div>';
        }
      });
    });
  }

  /* ---- OET / IELTS score checker ---- */
  function wireChecker() {
    var form = document.querySelector("#score-checker");
    if (!form) return;
    var resultBox = form.querySelector("[data-result]");
    var req = {
      OET: { reading: 350, listening: 350, speaking: 350, writing: 300 },
      IELTS: { reading: 7, listening: 7, speaking: 7, writing: 6.5 }
    };
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var test = form.querySelector("[name=test]").value;
      var r = req[test];
      var labels = { reading: "Reading", listening: "Listening", speaking: "Speaking", writing: "Writing" };
      var rows = [];
      var allPass = true;
      Object.keys(r).forEach(function (band) {
        var input = form.querySelector("[name=" + band + "]");
        var val = parseFloat(input.value);
        var pass = !isNaN(val) && val >= r[band];
        if (!pass) allPass = false;
        rows.push(
          '<li class="' + (isNaN(val) ? "" : (pass ? "ok" : "short")) + '">' +
          '<span>' + labels[band] + '</span>' +
          '<span class="verdict">' + (isNaN(val) ? "Enter a score" : (pass ? "Meets NCNZ minimum (" + r[band] + ")" : "Below NCNZ minimum of " + r[band])) + '</span>' +
          '</li>'
        );
      });
      resultBox.innerHTML = '<ul class="tool__result">' + rows.join("") + '</ul>' +
        '<p class="tool__summary">' + (allPass
          ? "All bands meet the Nursing Council of New Zealand's minimum requirement. Well done — talk to us about locking in your OSCE date."
          : "One or more bands are short of NCNZ's minimum. That's completely fixable — this is exactly what our " + test + " coaching targets.") + '</p>';
      resultBox.hidden = false;
    });
  }

  /* ---- contact / enquiry form (static-friendly, no backend wired yet) ---- */
  function wireForms() {
    document.querySelectorAll("form[data-enquiry]").forEach(function (form) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        var status = form.querySelector(".form__status");
        if (!form.checkValidity()) { form.reportValidity(); return; }
        var data = new FormData(form);
        var summary = "New enquiry — " + (data.get("name") || "") + " (" + (data.get("course") || "general") + ")";
        if (status) {
          status.textContent = "Thanks — your enquiry is ready to send. Connect this form to your email/CRM to go live, or tap \u201cContinue on WhatsApp\u201d below.";
        }
        var waBtn = form.querySelector("[data-wa-submit]");
        if (waBtn) {
          var msg = "Kia ora, I'm " + (data.get("name") || "") + ". I'm interested in " + (data.get("course") || "your courses") + ". " + (data.get("message") || "");
          waBtn.href = "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(msg);
          waBtn.hidden = false;
        }
      });
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    wireContactLinks();
    wireNav();
    wireChooser();
    wireChecker();
    wireForms();
  });
})();
