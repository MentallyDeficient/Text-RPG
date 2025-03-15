from fabric import Connection

class OldTerminal:
    def __init__(self, host, username, password):
        self.mock_mode = False
        try:
            self.conn = Connection(host=host, user=username, connect_kwargs={
                "password": password
            })
            self.conn.run("echo Connection successful", hide=True)
        except Exception as e:
            print(f"Connection failed: {e}")
            self.mock_mode = True

    def enter(self):
        print("The terminal screen flickers...")
        while True:
            cmd = input("$ ").strip()
            if cmd == "exit":
                break
            if self.mock_mode:
                print(f"Mock Terminal: Simulated output for '{cmd}'")
                continue
            try:
                result = self.conn.run(cmd, hide=True, warn=True)
                print(result.stdout)
            except Exception as e:
                print(f"ERROR: {e}")
