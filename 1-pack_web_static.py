from fabric import task
from datetime import datetime
import os

@task
def do_pack(c):
    """Generates a .tgz archive from the contents of the web_static folder."""
    try:
        # Create the versions folder if it doesn't exist
        if not os.path.exists("versions"):
            c.local("mkdir versions")

        # Generate the archive name using the current timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = f"web_static_{timestamp}.tgz"

        # Pack the contents of web_static into the archive
        c.local(f"tar -cvzf versions/{archive_name} web_static")

        # Return the path of the generated archive
        return f"versions/{archive_name}"
    except Exception as e:
        print(f"Error: {e}")
        return None

