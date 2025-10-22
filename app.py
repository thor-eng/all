# Simple single-file Flask app that serves a normal HTML page (no external templates required)
# Save this as flask_simple_app.py and run: python flask_simple_app.py
# Requires: Flask (install with `pip install flask`)

from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Simple Flask HTML Page</title>
    <style>
      body { font-family: system-ui, -apple-system, 'Segoe UI', Roboto, Arial; padding: 2rem; background:#f7fafc; color:#111827 }
      .card { background: white; padding: 1.5rem; border-radius: 8px; box-shadow: 0 6px 18px rgba(15,23,42,0.08); max-width:800px; margin: 0 auto }
      h1 { margin-top: 0 }
    </style>
  </head>
  <body>
    <div class="card">
      <h1>Welcome to Flask!</h1>
      <p>This is a normal HTML    page rendered by a Flask app. You can change this text to anything you like.</p>
      <p>Example list:</p>
      <ul>
        <li>Plain HTML content</li>
        <li>Served from a single-file Flask app</li>
        <li>Easy to extend with templates or static files</li>
      </ul>
    </div>
  </body>
</html>
"""

@app.route("/")
def index():
    # render_template_string is handy for quick demos; swap to render_template with a separate file
    return render_template_string(HTML_PAGE)

if __name__ == "__main__":
    app.run(port="5001",debug=True)
