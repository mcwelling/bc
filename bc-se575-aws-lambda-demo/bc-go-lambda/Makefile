.PHONY: build clean deploy

build:
	env GOOS=linux go build -ldflags="-s -w" -o bin/bc-go-lambda src/main.go

clean:
	rm -rf ./bin ./vendor

deploy: clean build
	sls deploy --verbose
