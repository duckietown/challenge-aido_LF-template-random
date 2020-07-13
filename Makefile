repo=challenge-aido_lf-template-random
# repo=$(shell basename -s .git `git config --get remote.origin.url`)
branch=$(shell git rev-parse --abbrev-ref HEAD)
tag=duckietown/$(repo):$(branch)

build:
	docker build --pull -t $(tag) .

build-no-cache:
	docker build --pull -t $(tag)  --no-cache .

push: build
	docker push $(tag)


update-reqs: # todo

submit: update-reqs
	dts challenges submit

submit-bea: update-reqs
	dts challenges submit --impersonate 1639 --challenge all --retire-same-label
