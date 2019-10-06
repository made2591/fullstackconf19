# FullStackConf - Torino 2019

This is out full stack solution to code from everywhere using Visual Code Studio. Many thanks to [github.com/cdr/code-server](https://github.com/cdr/code-server).

- [https://github.com/made2591/fullstackconf19/blob/master/speech/speech.pdf](https://github.com/made2591/fullstackconf19/blob/master/slides/speech.pdf) you can find a brief explanation of repo content.
- [https://madeddu.xyz/posts/aws/cloudformation/traefik-single-to-multi-tenant/](https://madeddu.xyz/posts/aws/cloudformation/traefik-single-to-multi-tenant/) you can find a blog post about original template.
- [https://madeddu.xyz/posts/aws/cloudformation/immutable-vsc/](https://madeddu.xyz/posts/aws/cloudformation/immutable-vsc/) you can find a blog post about multitenancy template.

## Architecture schemas

![](https://github.com/made2591/fullstackconf19/blob/master/slides/img/architecture.png)

## Requirements

* SAM CLI
* [Python 3 installed](https://www.python.org/downloads/)
* [Docker installed](https://www.docker.com/community-edition)

### Setup and deploy process

Firstly, we need a `S3 bucket` where we can upload our Lambda functions packaged as ZIP before we deploy anything - If you don't have a S3 bucket to store code artifacts then this is a good time to create one:

```bash
aws s3 mb s3://BUCKET_NAME
```

Next, run the following command to package our Lambda function to S3:

```bash
sam package \
    --output-template-file packaged.yaml \
    --s3-bucket REPLACE_THIS_WITH_YOUR_S3_BUCKET_NAME
```

Next, the following command will create a Cloudformation Stack and deploy your SAM resources.

```bash
sam deploy \
    --template-file packaged.yaml \
    --stack-name sam-app \
    --capabilities CAPABILITY_IAM
```

> **See [Serverless Application Model (SAM) HOWTO Guide](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-quick-start.html) for more details in how to get started.**

After deployment is complete you can run the following command to retrieve the API Gateway Endpoint URL:

```bash
aws cloudformation describe-stacks \
    --stack-name sam-app \
    --query 'Stacks[].Outputs[?OutputKey==`HelloWorldApi`]' \
    --output table
```

### Authors

* **Matteo Madeddu** - [Blog](https://madeddu.xyz/), [Github](https://github.com/made2591/), [LinkedIn](https://www.linkedin.com/in/mmadeddu/)
* **Guido Nebiolo** - [Github](https://github.com/guidonebiolo/), [LinkedIn](https://www.linkedin.com/in/guidonebiolo/)

Thank you for your interest!

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

* Fix architecture schemas
* Inspiration
* etc