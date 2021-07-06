""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.lhelp$")
async def usit(e):
    await e.edit(
        f"**Hai Lord {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.help` Atau Bisa Minta Bantuan Ke:\n"
        "\n[Telegram](t.me/liualvinas)"
        "\n[Repo](https://github.com/kenzx23/KEN-UBOT)"
        "\n[Instagram](Instagram.com/acxken._)")


@register(outgoing=True, pattern="^.vars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/kenzx23/KEN-UBOT/KEN-UBOT/varshelper.txt)")


CMD_HELP.update({
    "kenhelper":
    "`.lordhelp`\
\nPenjelasan: Bantuan Untuk KEN-UBOT.\
\n`.lordvar`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
