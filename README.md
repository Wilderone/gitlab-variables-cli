### glvar - simple utility for managing gitlab CI variables
**Strongly recomended to use containerized version**

There are two ways to provide your credentials:
* With environment variables GITLAB_URL, GITLAB_PRIVATE_TOKEN
* With .ini file and GITLAB_CREDENTIALS variable with path to the file

### Docker installation:

```
docker pull wilderone/glvar
```

*optional* set variables to control behavior of file mounts
*optional* use alias to simplify usage
```
MOUNT_CREDS="-v ~/credentials.ini:/app/credentials.ini"
MOUNT_VARS="-v ~/variables.json:/app/variables.json"
PROJECT="-e CLI_GITLAB_PROJECT=base-images"
DEFINE_CREDENTIALS="-e GITLAB_CREDENTIALS=/app/credentials.ini"

alias glvar='docker run -ti --rm ${MOUNT_CREDS} ${MOUNT_VARS} ${PROJECT} ${DEFINE_CREDENTIALS} wilderone/glvar'

glvar -l
glvar -p PROJECT_NAME -a KEY=VALUE
glvar -f /app/variables.json
```

**Important!**
.ini file should have this format:

```
[GITLAB]
GITLAB_URL=https://example.gitlab.com
GITLAB_PRIVATE_TOKEN=YOUR_TOKEN
```


See --help for list of available keys and instructions


