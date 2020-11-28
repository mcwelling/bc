## AWS LAMBDA FUNCTIONS

### Prep and Description
In order to setup this project you will need a few things:

* Node.js - install from web or homebrew (mac)
* GoLang - install from web or homebrew (mac)
* Python 3.8+ - install from web or homebrew (mac)
* Serverless Framework.  Install with yarn (`yarn global add serverless`) or npm (`npm install serverless -g`)

* The AWS cli - instructions here [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html]([bar](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html))

Before attempting to deploy anything using serverless make sure you can connect to your aws account.  For example test with `aws s3 ls` 

## AWS API Gateway Setup

In the `api-gw` directory there is a serverless script that will provision the required AWS API Gateway components.  To run it `sls deploy`.  Verify that the gateway is properly setup in the AWS console.  You should se an API Gateway named `BCApiGW` in the list of gateways, and you should also see resources for `\api\go` and `\api\python` created when you drill in.   Notice that no integrations have been setup at this point, just the shell.

If you want to see more about what is going on you can navigate over to cloud formation and drill into the `bc-api-gw-dev` stack. You can explore exactly what was provisioned.  Also go to the `Outputs` tab at the top and you can see a number of exported names that begin with `BcApiGateway-`.  We will be referring to these when we deploy the go and python services. 

## Test and Deploy the Go Lambda

Move into the `\bc-go-lambda` directory. Install the serverless offline plugin - `sls plugin install --name serverless-offline` then build the service `make build`.  This will create a linux binary in the `bin` directory.

If you want to test the lambda locally you will need to have docker installed.  Once you have docker installed to test run `sls offline --useDocker`.  To test go to your browser and navigate to `http://localhost:3000/dev/api/go?q=DATA_IN_BLOCK&p=PARENT_BLOCK_ID&b=BLOCK_ID&x=0000&m=1000000`.  Note you can adjust any parameters that you want.  The `x` parameter is the complexity - leading zeros, and the `m` parameter is the max-tries or when the service will give up on trying to find a solution.

Now you are able to deploy to AWS in one command: `sls deploy`.  In the `serverless.yml` file you will see references to the cloudformation variables we setup during the api gateway deployment. 

## Test and Deploy the Python Lambda

Move into the `\bc-go-python` directory. Install the serverless offline plugin - `sls plugin install --name serverless-offline`.

Unlike the go example, python does not require a build step. To test run `sls offline`.  Then navigate to http://localhost:3000/dev/api/python?q=DATA_IN_BLOCK&p=PARENT_BLOCK_ID&b=BLOCK_ID&x=0000&m=1000000.  Again you can adjust parameters as you see fit.

Deploy to AWS via `sls deploy`
