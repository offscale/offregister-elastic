from offregister_fab_utils.ubuntu.systemd import restart_systemd
from patchwork.files import append


def install0(**kwargs):
    installed = lambda: c.run(
        "dpkg-query --showformat='${Version}' --show elasticsearch", hide=True
    )

    if c.sudo("dpkg -s elasticsearch", hide=True, warn=True).exited != 0:
        c.sudo(
            "wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-key add -"
        )

        append(
            "/etc/apt/sources.list.d/elasticsearch.list",
            "deb http://packages.elasticsearch.org/elasticsearch/{}/debian stable main".format(
                kwargs["VERSION"][: kwargs["VERSION"].rfind(".")]
                if kwargs["VERSION"].count(".") == 3
                else kwargs["VERSION"]
            ),
            use_sudo=True,
        )
        c.sudo("apt update")
        c.sudo("apt-get install -y elasticsearch={}".format(kwargs["VERSION"]))
        if kwargs.get("NO_UPGRADE"):
            c.sudo("apt-mark hold elasticsearch")
        restart_systemd("elasticsearch")

        return "elasticsearch {} installed".format(installed())

    return "[Already] elasticsearch {} installed".format(installed())
