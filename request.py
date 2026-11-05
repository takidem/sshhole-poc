
import argparse
import paramiko

def check(host, port, user):
    transport = paramiko.Transport((host, port))

    try:
        transport.start_client(timeout=5)

        print(f"SSH Version: {transport.remote_version}")

        try:
            transport.auth_none(user)
            print("Authentication: none accepted")
        except paramiko.BadAuthenticationType as e:
            print(f"Auth methods: {e.allowed_types}")
        except paramiko.AuthenticationException:
            print("Authentication required")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        transport.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", required=True)
    parser.add_argument("--port", type=int, default=22)
    parser.add_argument("--user", required=True)
    args = parser.parse_args()

    check(args.host, args.port, args.user)

