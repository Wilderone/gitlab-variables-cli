import sys

if '--help' in sys.argv:
    print('''
    This util was created to help you manage CI variables in Gitlab
    Use environment variables GITLAB_URL and GITLAB_PRIVATE_TOKEN for authorization.
    Also you can provide .ini with [GITLAB] header, example:
    > cat /app/credentials.ini
    [GITLAB]
    GITLAB_URL=https://example.gitlab.com
    GITLAB_PRIVATE_TOKEN=YOUR_TOKEN

    Use GITLAB_CREDENTIALS variable to define path

    Project or group provided via cli (-p / -g) has the highest priority than ENV variables
    -p  -  set project name (-p MyProject) or use CLI_GITLAB_PROJECT environment variable
    -g  -  set group name (-g MyGroup) or use CLI_GITLAB_GROUP environment variable
    -l  -  list of variables
    -la -  list of variables in every project of group (use with -g GROUP_NAME) 
    -a  -  add variable (-a KEY=VALUE), use -f for miltiple variables
    -f  -  add variables from JSON file (-f /path/to/file)
    -m  -  mask added variable(s). Be sure variable meet regular expression requirements.
    -rm -  remove variable (-rm KEY), use list to delete multiple vars (-rm KEY1,KEY2,KEY3)
    -rmf - remove variables, passed from JSON ( {"KEY":"VALUE"} )file (-rmf /path/to/file) 
    -cv -  change value of variable (-cv NAME=NEW_VALUE)

     ''')
    sys.exit(1)
