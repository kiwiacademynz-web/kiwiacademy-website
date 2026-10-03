/* ==========================================================
  DREAMVISION — shared site behaviour
   ========================================================== */
(function () {
  "use strict";
  var C = window.KNA || {};

  /* ---- wire up every data-wa / data-tel / data-email link ---- */
  function wireContactLinks() {
    var waMsg = "Hello, I'd like to learn more about DREAMVISION's services.";
    document.querySelectorAll("[data-wa]").forEach(function (el) {
      var msg = el.getAttribute("data-wa-msg") || waMsg;
      el.href = "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(msg);
      if (el.target === undefined || !el.hasAttribute("target")) el.target = "_blank";
      el.rel = "noopener";
    });
    document.querySelectorAll("[data-phone-australia]").forEach(function (el) {
      el.href = "tel:" + C.phoneAustralia;
    });
    document.querySelectorAll("[data-phone-india]").forEach(function (el) {
      el.href = "tel:" + C.phoneIndia;
    });
    document.querySelectorAll("[data-email]").forEach(function (el) {
      el.href = "mailto:" + C.email;
      if (el.hasAttribute("data-email-text")) el.textContent = C.email;
    });
    document.querySelectorAll("[data-social]").forEach(function (el) {
      var key = el.getAttribute("data-social");
      if (C.social && C.social[key]) el.href = C.social[key];
      else el.hidden = true;
    });
    document.querySelectorAll("[data-hours]").forEach(function (el) { el.textContent = C.hours; });
    document.querySelectorAll("[data-address-australia]").forEach(function (el) { el.textContent = C.addressAustralia; });
    document.querySelectorAll("[data-address-muvattupuzha]").forEach(function (el) { el.textContent = C.addressMuvattupuzha; });
    document.querySelectorAll("[data-address-kannur]").forEach(function (el) { el.textContent = C.addressKannur; });
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
        var fields = [
          ["Name", data.get("name")],
          ["Phone / WhatsApp", data.get("phone")],
          ["Email", data.get("email")],
          ["Service / role", data.get("course")],
          ["Message", data.get("message")]
        ];
        var msg = "Kia ora, I'd like to get in touch with DREAMVISION.\n\n" +
          fields.filter(function (field) { return field[1] && String(field[1]).trim(); })
            .map(function (field) { return field[0] + ": " + String(field[1]).trim(); })
            .join("\n");
        if (!C.whatsapp) {
          if (status) status.textContent = "WhatsApp is not configured. Please contact us by phone or email.";
          return;
        }
        window.location.href = "https://wa.me/" + C.whatsapp + "?text=" + encodeURIComponent(msg);
      });
    });
  }

  /* ---- instant website assistant ---- */
  function wireAssistant() {
    var assistant = document.createElement("section");
    assistant.className = "site-assistant";
    assistant.innerHTML =
      '<div class="assistant-panel" id="assistant-panel" role="dialog" aria-labelledby="assistant-title" aria-modal="false" hidden>' +
        '<header class="assistant-panel__head"><div><h2 id="assistant-title">DreamVision assistant</h2><p>Here to help you explore your next step</p></div><button class="assistant-close" type="button" aria-label="Close assistant">&times;</button></header>' +
        '<p class="assistant-disclaimer">Instant answers based on this website. Always confirm current rules with the official regulator.</p>' +
        '<div class="assistant-messages" role="log" aria-live="polite" aria-relevant="additions text"><p class="assistant-message">Kia ora! I’m DreamVision’s virtual assistant. Thanks for stopping by. I can help you explore our courses and pathways. What would you like to know?</p></div>' +
        '<div class="assistant-quick" aria-label="Suggested questions">' +
        '<button type="button" data-topic="OET course">OET course</button><button type="button" data-topic="IQN exam">IQN exam</button>' +
        '<button type="button" data-topic="OSCE NZ exam">OSCE NZ</button><button type="button" data-topic="NCLEX-RN course">NCLEX-RN</button>' +
        '<button type="button" data-topic="AHPRA self-check">AHPRA self-check</button>' +
        '</div>' +
        '<form class="assistant-composer"><label class="skip-link" for="assistant-input">Ask a question</label><input id="assistant-input" name="question" maxlength="500" placeholder="Type your question…" autocomplete="off" required><button class="assistant-send" type="submit">Ask</button></form>' +
      '</div>' +
      '<button class="assistant-launcher" type="button" aria-expanded="false" aria-controls="assistant-panel"><span class="assistant-launcher__status" aria-hidden="true"></span><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H10l-5 4v-4.8a2.5 2.5 0 0 1-1-2z"/><path d="M8 8h8M8 11.5h5"/></svg><span>Ask Me</span></button>';
    document.body.appendChild(assistant);

    var panel = assistant.querySelector(".assistant-panel");
    var launcher = assistant.querySelector(".assistant-launcher");
    var close = assistant.querySelector(".assistant-close");
    var messages = assistant.querySelector(".assistant-messages");
    var quick = assistant.querySelector(".assistant-quick");
    var composer = assistant.querySelector(".assistant-composer");
    var input = assistant.querySelector("#assistant-input");
    var brandLink = document.querySelector(".site-header .brand");
    var siteRoot = new URL(".", brandLink ? brandLink.href : window.location.href).href;

    function addMessage(text, fromUser, href, linkText) {
      var bubble = document.createElement("p");
      bubble.className = "assistant-message" + (fromUser ? " assistant-message--user" : "");
      bubble.textContent = text;
      if (href) {
        appendAssistantLink(bubble, href, linkText || "Open the official AHPRA self-check");
      }
      messages.appendChild(bubble);
      messages.scrollTop = messages.scrollHeight;
    }

    function appendAssistantLink(container, href, text) {
      var link = document.createElement("a");
      link.href = href.indexOf("https://") === 0 ? href : new URL(href, siteRoot).href;
      link.textContent = text;
      if (href.indexOf("https://") === 0) {
        link.target = "_blank";
        link.rel = "noopener noreferrer";
      }
      container.appendChild(document.createElement("br"));
      container.appendChild(link);
    }

    function addSupportLinks() {
      var bubble = document.createElement("p");
      bubble.className = "assistant-message";
      bubble.appendChild(document.createTextNode("Customer support: "));
      appendAssistantLink(bubble, "mailto:" + C.email, C.email);
      if (C.phoneIndia) appendAssistantLink(bubble, "tel:" + C.phoneIndia, C.phoneIndia);
      if (C.whatsapp) appendAssistantLink(bubble, "https://wa.me/" + C.whatsapp, "Message customer support on WhatsApp");
      bubble.appendChild(document.createElement("br"));
      bubble.appendChild(document.createTextNode("Hours: " + C.hours + ". Kerala offices: " + C.addressMuvattupuzha + "; " + C.addressKannur + "."));
      messages.appendChild(bubble);
      messages.scrollTop = messages.scrollHeight;
    }

    function getAnswer(question) {
      var q = question.toLowerCase().trim();
      if (/^(hi|hello|hey|kia ora|good morning|good afternoon|good evening)( there)?[!,. ]*(how are you)?[!,. ]*$/.test(q)) {
        return "Hi! Thanks for contacting DreamVision 😊 How can I help you today? You can ask me about OET, IQN, OSCE NZ, NCLEX-RN, AHPRA, or choosing a pathway.";
      }
      if (/^(thanks|thank you|thx|cheers)[!,. ]*$/.test(q)) {
        return "You’re very welcome! I’m glad I could help. Is there anything else about your course or pathway you’d like to know?";
      }
      if (/\b(how are you|how's it going)\b/.test(q)) {
        return "Thanks for asking! I’m here and ready to help 😊 What are you hoping to find out today?";
      }
      var encouragement = /\b(worried|anxious|nervous|scared|stressed|overwhelmed|confused|not sure|unsure|struggling)\b/.test(q)
        ? "I understand this can feel like a lot to work through. Let’s take it one step at a time. "
        : "";
      if (/\b(nclex|nclex-rn)\b/.test(q)) {
        return encouragement + "NCLEX-RN is a licensure exam used by nursing regulators in the United States and Canada. DreamVision offers preparation; our customer support team can confirm the current format, schedule and fees. Your target regulator decides eligibility and licensing. Would you like to know what to check before choosing a course?";
      }
      if (/\b(osce|clinical exam|christchurch)\b/.test(q)) {
        return encouragement + "For OSCE NZ, we can help you practise clinical stations, communication and timed mock exams online or in person. The official NCNZ orientation and OSCE take place in person in Christchurch, and NCNZ decides who is invited. Are you preparing for an upcoming assessment?";
      }
      if (/\b(iqn|pearson|theor|medication safety)\b/.test(q)) {
        return encouragement + "The NCNZ IQN theoretical exam covers medication safety (Part A) and nursing knowledge (Part B), and is taken at an accredited Pearson VUE centre. DreamVision offers online preparation and timed mock exams. Have you booked your exam yet, or are you still planning your preparation?";
      }
      if (/\b(oet|ielts|english|score|band)\b/.test(q)) {
        return encouragement + "If you’re preparing for OET, DreamVision offers one-to-one online coaching across all four sub-tests. The website lists NCNZ’s OET minimums as 350 in Reading, Listening and Speaking and 300 in Writing, or IELTS Academic 7.0/7.0/7.0/6.5. Please confirm current requirements with NCNZ before booking. Which test are you working towards?";
      }
      if (/\bahpra\b|\baustralian registration\b|\bself.?check\b/.test(q)) {
        return "For Australian nursing registration, a good first step is AHPRA’s official self-check. It can help you identify a possible pathway, though it isn’t a registration decision. Would you like the link?";
      }
      if (/\banmac\b/.test(q)) {
        return encouragement + "DreamVision can help you understand and prepare for an ANMAC skills assessment. Requirements depend on your circumstances, so please check the current instructions with ANMAC. Are you starting an assessment or already working through one?";
      }
      if (/\b(fee|fees|cost|price|payment)\b/.test(q)) {
        return "That’s a fair thing to check before making plans. Fees depend on the course and your requirements, so please contact our team for current details and a written breakdown. Official exam or regulator fees may be separate. Which course are you interested in?";
      }
      if (/\b(visa|immigration|pr|permanent residency)\b/.test(q)) {
        return "It’s important to get the right guidance for immigration matters. DreamVision offers pathway support, but advice should come from a licensed immigration adviser or the relevant government authority. Visa decisions are made by the relevant authority.";
      }
      if (/\b(ncnz|nursing council)\b/.test(q) ||
          (/\b(registration|register)\b/.test(q) && /\b(new zealand|nz|nurse)\b/.test(q))) {
        return encouragement + "NCNZ reviews each internationally qualified nurse’s application and decides whether a competence assessment is needed. If you’re directed to one, the pathway includes a theoretical exam and then the in-person orientation and OSCE in Christchurch. English-language evidence is also required. Have you already applied to NCNZ, or are you just getting started?";
      }
      if (/\b(study|student|pre.?arrival|new zealand|australia)\b/.test(q)) {
        return encouragement + "DreamVision supports study pathways in New Zealand and Australia, pre-arrival planning and nursing registration preparation. Which destination and goal are you considering? I’ll point you to the most relevant information I have.";
      }
      if (/\b(contact|phone|email|location|address|kerala|muvattupuzha|kannur|talk|human|team)\b/.test(q)) {
        return "Of course — our customer support team can help with that. Support hours are " + C.hours + ", and our Kerala offices are in Muvattupuzha and Kannur. I’ll share the contact options below.";
      }
      if (/\bwhat can you\b|\bwhat courses\b|\bhelp me choose\b|\bwhere do i start\b/.test(q)) {
        return "Absolutely — we can figure out a useful next step together. I can help with OET, IQN, OSCE NZ, NCLEX-RN, AHPRA, ANMAC, study pathways and fees. What destination or exam are you working towards?";
      }
      return encouragement + "I’m sorry, I don’t have reliable information about that topic just yet. I don’t want to guess and mislead you. DreamVision’s customer support team can help — I’ll share their contact details below.";
    }

    function answerQuestion(question) {
      var answer = getAnswer(question);
      var q = question.toLowerCase();
      var href = "";
      var linkText = "";
      if (/\bahpra\b|\bself.?check\b/.test(q)) {
        href = "https://portal.ahpra.gov.au/portal/s/self-check";
        linkText = "Open the official AHPRA self-check";
      } else if (/\bnclex\b/.test(q)) {
        href = "best-nclex-rn-training-in-kerala.html";
        linkText = "View NCLEX-RN course information";
      } else if (/\bosce\b/.test(q)) {
        href = "best-osce-training-in-kerala.html";
        linkText = "View OSCE NZ course information";
      } else if (/\biqn\b|\bpearson\b|\btheoretical exam\b/.test(q)) {
        href = "best-iqn-training-in-kerala.html";
        linkText = "View IQN course information";
      } else if (/\boet\b|\bielts\b/.test(q)) {
        href = "best-oet-training-in-kerala.html";
        linkText = "View OET course information";
      } else if (/\b(ncnz|nursing council)\b/.test(q) ||
          (/\b(registration|register)\b/.test(q) && /\b(new zealand|nz|nurse)\b/.test(q))) {
        href = "courses/index.html";
        linkText = "Compare New Zealand nursing courses";
      }
      addMessage(question, true);
      addMessage(answer, false, href, linkText);
      if (/\b(contact|phone|email|location|address|kerala|muvattupuzha|kannur|talk|human|team)\b/.test(q) ||
          answer.indexOf("isn't covered in the assistant") !== -1) {
        addSupportLinks();
      }
    }

    function openPanel() {
      panel.hidden = false;
      launcher.setAttribute("aria-expanded", "true");
      input.focus();
    }

    function closePanel() {
      panel.hidden = true;
      launcher.setAttribute("aria-expanded", "false");
      launcher.focus();
    }

    launcher.addEventListener("click", function () {
      if (panel.hidden) openPanel();
      else closePanel();
    });
    close.addEventListener("click", closePanel);
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !panel.hidden) closePanel();
    });
    quick.addEventListener("click", function (event) {
      var button = event.target.closest("button");
      if (!button) return;
      answerQuestion(button.getAttribute("data-topic"));
    });
    composer.addEventListener("submit", function (event) {
      event.preventDefault();
      var question = input.value.trim();
      if (!question) return;
      answerQuestion(question);
      input.value = "";
      input.focus();
    });
  }

  function wireSectionReveals() {
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    var sections = document.querySelectorAll("main > .topo, main > .section, main > section, .cta-band");
    if (!("IntersectionObserver" in window)) return;
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.remove("reveal-pending");
        entry.target.classList.add("reveal-visible");
        observer.unobserve(entry.target);
      });
    }, { threshold: 0.08, rootMargin: "0px 0px -32px 0px" });
    sections.forEach(function (section) {
      section.classList.add("reveal-pending");
      observer.observe(section);
    });
  }

  function wireMetricCounters() {
    var metrics = document.querySelectorAll(".metrics-grid [data-count]");
    if (!metrics.length || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    if (!("IntersectionObserver" in window) || !("requestAnimationFrame" in window)) return;

    var formatter = new Intl.NumberFormat("en", { maximumFractionDigits: 1 });
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        observer.unobserve(entry.target);

        var metric = entry.target;
        var target = Number(metric.getAttribute("data-count"));
        var decimals = Number(metric.getAttribute("data-count-decimals") || 0);
        var suffix = metric.getAttribute("data-count-suffix") || "";
        if (!Number.isFinite(target) || !Number.isFinite(decimals)) return;

        var startTime;
        var scale = Math.pow(10, decimals);
        function updateCount(timestamp) {
          if (startTime === undefined) startTime = timestamp;
          var progress = Math.min((timestamp - startTime) / 1600, 1);
          var easedProgress = 1 - Math.pow(1 - progress, 3);
          var value = Math.round(target * easedProgress * scale) / scale;
          metric.textContent = formatter.format(value) + suffix;
          if (progress < 1) window.requestAnimationFrame(updateCount);
        }

        metric.textContent = formatter.format(0) + suffix;
        window.requestAnimationFrame(updateCount);
      });
    }, { threshold: 0.35 });

    metrics.forEach(function (metric) { observer.observe(metric); });
  }

  document.addEventListener("DOMContentLoaded", function () {
    wireContactLinks();
    wireNav();
    wireChooser();
    wireChecker();
    wireForms();
    wireAssistant();
    wireSectionReveals();
    wireMetricCounters();
  });
})();
