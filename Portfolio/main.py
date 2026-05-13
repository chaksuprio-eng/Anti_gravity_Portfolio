import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler

def run_server(port=8000):
    print(f"\n[bold nebula]⟐ Antigravity Portfolio Server[/bold nebula]")
    print(f"Serving at: [link=http://localhost:{port}]http://localhost:{port}[/link]")
    print("Press Ctrl+C to stop.\n")
    
    server_address = ('', port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping server...")
        httpd.server_close()

def show_status():
    print("\n[bold nebula]⟐ Workspace Status[/bold nebula]")
    files = ["index.html", "requirements.txt", "main.py", "assets/aria.png"]
    for f in files:
        exists = "✅" if os.path.exists(f) else "❌"
        print(f"{exists} {f}")

def main():
    # Simple fallback if rich is not installed
    try:
        from rich import print
        from rich.console import Console
        from rich.panel import Panel
    except ImportError:
        # Simple print fallback
        def print_fallback(*args, **kwargs):
            import builtins
            text = " ".join(map(str, args))
            # Strip rich tags
            import re
            text = re.sub(r'\[.*?\]', '', text)
            builtins.print(text)
        
        # Override global print for this scope
        globals()['print'] = print_fallback

    if len(sys.argv) < 2:
        print("\n[bold nebula]⟐ Antigravity Portfolio Manager[/bold nebula]")
        print("Usage: python main.py [command]")
        print("\nCommands:")
        print("  serve   - Start local development server")
        print("  status  - Check workspace health")
        print("  info    - Show project details")
        return

    cmd = sys.argv[1].lower()
    if cmd == "serve":
        run_server()
    elif cmd == "status":
        show_status()
    elif cmd == "info":
        print("\n[bold nebula]⟐ Antigravity Project Info[/bold nebula]")
        print("Project: Futuristic Portfolio")
        print("Version: 1.0.0")
        print("Status: Active")
    else:
        print(f"Unknown command: {cmd}")

if __name__ == "__main__":
    main()
