The purpose of this repo is to provide an example of a dev environment container which generates an xgboost model, and a prod environment container which consumes the model and produces predictions in the form of a .csv file.

First make a docker hub account and create a repo called `modeling_demo`, and then clone this repo. The build process for both containers may take up to an hour.

```
> cd </path/to/dev>

> docker build -t <username>/modeling_demo:dev-0.0.1 .

> docker push <username>/modeling_demo:dev-0.0.1

> cd </path/to/prod>

> docker build -t <username>/modeling_demo:prod-0.0.1 .

> docker push <username>/modeling_demo:prod-0.0.1

```

Once that is completed you can run the dev environment container by 

``` 

> docker run -it -p 8888:8888 <username>/modeling_demo:dev-0.0.1

root@<container_id>:/app# jupyter notebook --ip 0.0.0.0 --no-browser --allow-root

```

You can then run the jupyter notebooks. Use the option which looks like `http://127.0.0.1:8888/<token>`. When you are finished enter `\\wsl$\docker-desktop-data\data\docker\volumes` on Windows or `/var/lib/docker/volumes/` on macOS or other UNIX OS into your file explorer. Sort by date modified to find the latest folder and inside you will find `xgb_reg.pkl` inside the `_data` folder. Move the pickle file somewhere else, such as the repo folder.

Now run the prod container and it will print the mean squared error of the model:

```

docker run -v <path/to/xgb_reg.pkl>:/app/xgb_reg.pkl <username>/modeling_demo:prod-0.0.1

0.2401475171547707


```

Again check the latest modified folder in the docker volumes and you will find `predictions.csv`
