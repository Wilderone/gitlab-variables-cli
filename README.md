### glvar - simple utility for managing gitlab CI variables
**Strongly recomended to use containerized version**

There are two ways to provide your credentials:
* With environment variables GITLAB_URL, GITLAB_PRIVATE_TOKEN
* With .ini file and GITLAB_CREDENTIALS variable with path to the file

**Important!**
.ini file should have this format:

```
[GITLAB]
GITLAB_URL=https://example.gitlab.com
GITLAB_PRIVATE_TOKEN=YOUR_TOKEN
```

Use aliases for simplify of usage:

```
MOUNT_CREDS="-v ~/credentials.ini:/app/credentials.ini"
MOUNT_VARS="-v ~/variables.json:/app/variables.json"
PROJECT="-e CLI_GITLAB_PROJECT=base-images"
DEFINE_CREDENTIALS="-e GITLAB_CREDENTIALS=/app/credentials.ini"

alias glvar='docker run -ti --rm ${MOUNT_CREDS} ${MOUNT_VARS} ${PROJECT} ${DEFINE_CREDENTIALS} glvar'

glvar -l
glvar -p PROJECT_NAME -a KEY=VALUE
glvar -f /app/variables.json
```

See --help for list of available keys and instructions


