import os

def add_chroot_segment():

    if os.getenv('SCHROOT_SESSION_ID'):
        powerline.append(" chroot ", Color.SSH_FG, Color.SSH_BG)

add_chroot_segment()
