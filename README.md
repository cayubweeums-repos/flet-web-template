# flet-web-template
Flet project template that ships with the appwrite backend in the 'stack'


# Steps to get working

1. Clone the repo & cd into it
2. Run appwrite docker run command on server
```shell
docker run -it --rm \
    --volume /var/run/docker.sock:/var/run/docker.sock \
    --volume "$(pwd)"/appwrite:/usr/src/code/appwrite:rw \
    --entrypoint="install" \
    appwrite/appwrite:1.6.0
```
3. Follow prompts
4. Run `docker-compose up`
5. Go to `https://<your-appwrite-ip>`
- Make an account and then an org
- Go into the org, make a new project, then go into it and go down to the bottom of the overview page under integrations and make a new API key
6. Make and configure API key
- Give the API key permissions you will need the web app to have when communicating with the appwrite backend and then create it
- This is what you will use in your frontend/client side to configure backend communication
