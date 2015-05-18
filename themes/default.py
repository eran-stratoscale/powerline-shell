class DefaultColor:
    """
    This class should have the default colors for every segment.
    Please test every new segment with this theme first.
    """
    USERNAME_FG = 250
    USERNAME_BG = 240
    USERNAME_ROOT_BG = 124

    HOSTNAME_FG = 250
    HOSTNAME_BG = 238

    HOME_SPECIAL_DISPLAY = False
    HOME_BG = 31  # blueish
    HOME_FG = 15  # white
    PATH_BG = 240  # dark grey
    PATH_FG = 250  # light grey
    CWD_FG = 254  # nearly-white grey
    SEPARATOR_FG = 244

    READONLY_BG = 124
    READONLY_FG = 254

    ENV_BG = 70
    ENV_FG = 15
    NO_ENV_BG = 110
    NO_ENV_FG = 0

    SSH_BG = 166 # medium orange
    SSH_FG = 254

    REPO_CLEAN_BG = 236  # a light green color
    REPO_CLEAN_FG = 410  # black
    REPO_DIRTY_BG = 236  # pink/red
    REPO_DIRTY_FG = 166  # orange
    REPO_ADDED_BG = 236  #
    REPO_ADDED_FG = 185  # yellow

    REPO_BG = 236  # pink/red
    REPO_FG = 250  # white

    TIME_BG = 31 #4
    TIME_FG = 254 #254

    JOBS_FG = 39
    JOBS_BG = 238

    CMD_PASSED_BG = 236
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 88
    CMD_FAILED_FG = 15

    SVN_CHANGES_BG = 148
    SVN_CHANGES_FG = 22  # dark green

    VIRTUAL_ENV_BG = 35  # a mid-tone green
    VIRTUAL_ENV_FG = 00

class Color(DefaultColor):
    """
    This subclass is required when the user chooses to use 'default' theme.
    Because the segments require a 'Color' class for every theme.
    """
    pass
