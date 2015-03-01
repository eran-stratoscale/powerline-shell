import re
import os
import subprocess

PLUS_SIGN = '+'
UPDOWN_SIGN = u'\u21C5'
UP_SIGN = u'\u21E1'
DOWN_SIGN = u'\u21E3'

def get_git_status():
    has_pending_commits = True
    has_untracked_files = False
    status = ""
    output = subprocess.Popen(['git', 'status', '--ignore-submodules'], env={"LANG": "C", "HOME": os.getenv("HOME")}, stdout=subprocess.PIPE).communicate()[0]

    origin_status = re.findall(r"Your branch is (ahead|behind).*?(\d+) comm", output)
    if origin_status:
        status = " %d" % int(origin_status[0][1])
        if origin_status[0][0] == 'behind':
            status += DOWN_SIGN
        if origin_status[0][0] == 'ahead':
            status += UP_SIGN

    diverged = re.findall(r"and have (\d+) and (\d+) different commit each", output)
    if diverged:
        status = " %s%s%s" % (diverged[0][0], UPDOWN_SIGN, diverged[0][1])

    if output.find('nothing to commit') >= 0:
        has_pending_commits = False
    if output.find('Untracked files') >= 0:
        has_untracked_files = True

    return has_pending_commits, has_untracked_files, status


def add_git_segment():
    # See http://git-blame.blogspot.com/2013/06/checking-current-branch-programatically.html
    p = subprocess.Popen(['git', 'symbolic-ref', '-q', 'HEAD'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()

    if 'Not a git repo' in err:
        return

    branch_icon = '%s ' % powerline.branch
    if out:
        branch = out[len('refs/heads/'):].rstrip()
    else:
        branch = '(detached)'

    has_pending_commits, has_untracked_files, origin_position = get_git_status()
    branch += origin_position
    if has_untracked_files:
        branch += u' %s' % PLUS_SIGN

    bg = Color.REPO_CLEAN_BG
    fg = Color.REPO_CLEAN_FG
    if has_pending_commits:
        bg = Color.REPO_DIRTY_BG
        fg = Color.REPO_DIRTY_FG

    powerline.append(' %s' % branch_icon, fg, bg, separator='')
    powerline.append('%s ' % branch, Color.REPO_FG, Color.REPO_BG)


try:
    add_git_segment()
except OSError:
    pass
except subprocess.CalledProcessError:
    pass
