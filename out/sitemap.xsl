<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9"
  exclude-result-prefixes="s">
  <xsl:output method="html" encoding="UTF-8" indent="yes"
    doctype-system="about:legacy-compat"/>

  <xsl:template match="/">
    <html lang="en">
      <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title>DREAMVISION | Sitemap</title>
        <style>
          :root { color-scheme: light; font-family: Arial, sans-serif; color: #172d49; background: #f5f7fa; }
          body { margin: 0; padding: 48px 20px; }
          main { max-width: 900px; margin: 0 auto; }
          header { margin-bottom: 24px; }
          h1 { margin: 0 0 8px; font-size: clamp(1.8rem, 5vw, 2.5rem); }
          p { margin: 0; color: #526174; line-height: 1.6; }
          .table-wrap { overflow-x: auto; border: 1px solid #dce3eb; border-radius: 12px; background: #fff; }
          table { width: 100%; border-collapse: collapse; text-align: left; }
          th, td { padding: 14px 18px; border-bottom: 1px solid #e8edf2; }
          th { background: #edf2f7; color: #34445a; font-size: .85rem; letter-spacing: .04em; text-transform: uppercase; }
          tr:last-child td { border-bottom: 0; }
          td:first-child { width: 56px; color: #65758a; }
          a { color: #176b58; overflow-wrap: anywhere; }
          a:hover { color: #104c40; }
          footer { margin-top: 20px; font-size: .9rem; }
          @media (max-width: 520px) {
            body { padding: 28px 14px; }
            th, td { padding: 12px; }
          }
        </style>
      </head>
      <body>
        <main>
          <header>
            <h1>DREAMVISION sitemap</h1>
            <p>A directory of pages on dreamvisionedu.au, listed alphabetically.</p>
          </header>
          <div class="table-wrap">
            <table>
              <thead>
                <tr><th scope="col">#</th><th scope="col">Page</th><th scope="col">URL</th></tr>
              </thead>
              <tbody>
                <xsl:for-each select="s:urlset/s:url">
                  <xsl:sort select="s:loc"/>
                  <tr>
                    <td><xsl:value-of select="position()"/></td>
                    <td>
                      <xsl:choose>
                        <xsl:when test="s:loc = 'https://dreamvisionedu.au/'">Home</xsl:when>
                        <xsl:otherwise>
                          <xsl:value-of select="translate(substring-after(s:loc, 'https://dreamvisionedu.au/'), '-', ' ')"/>
                        </xsl:otherwise>
                      </xsl:choose>
                    </td>
                    <td><a href="{s:loc}"><xsl:value-of select="s:loc"/></a></td>
                  </tr>
                </xsl:for-each>
              </tbody>
            </table>
          </div>
          <footer><p><xsl:value-of select="count(s:urlset/s:url)"/> pages in this sitemap.</p></footer>
        </main>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
