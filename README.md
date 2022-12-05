The purpose of this repo is to provide an example of a dev environment container which generates an xgboost model, and a prod environment container which consumes the model and produces predictions in the form of a .csv file.

First make a docker hub account and create a repo called `modeling_demo`, and then clone this repo.

```
> cd </path/to/dev>

> docker build -t <username>/modeling_demo:dev-0.0.1 .

> docker push <username>/modeling_demo:dev-0.0.1

> cd </path/to/prod>

> docker build -t <username>/modeling_demo:prod-0.0.1 .

> docker push <username>/modeling_demo:prod-0.0.1

```

Once that is completed you can run the dev environment container by 