import docker

""" config """

ACTIVATION_CODE = "XXXX-XXXX-XXXX-XXXX-XXXX"
USERNAME = "admin"
PASSWORD = "changeme"

""" main """

BIND_IP = "127.0.0.1"
BIND_PORT = 8888


REPO_TAG = "tenable/nessus:latest-ubuntu"

dkr = docker.from_env()

print("\nNessus Docker\n")

print("  [+] Pulling Image..")
dkr.images.pull(
    repository=REPO_TAG.split(":")[0],
    tag=REPO_TAG.split(":")[1],
    all_tags=False
)

# clean
print("  [+] Cleaning Environment..")
nessus = dkr.containers.list(all=True, filters={"name": "nessus"})
if len(nessus) == 1:
    container = dkr.containers.get(nessus[0].id)
    # stop if running
    if container.attrs['State']['Running'] == True:
        container.kill()
    # remove
    container.remove(force=True)

# run
print("  [+] Running Container..")
dkr.containers.run(
    name="nessus",
    image=REPO_TAG,
    ports={'8834/tcp': (BIND_IP, BIND_PORT)},
    environment={
        "USERNAME": USERNAME,
        "PASSWORD": PASSWORD,
        "ACTIVATION_CODE": ACTIVATION_CODE,
    },
    restart_policy={"Name": "always"},
    detach=True
)

print(f"\nURL: https://{BIND_IP}:{BIND_PORT}")
