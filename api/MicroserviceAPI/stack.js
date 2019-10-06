const AWS = require('aws-sdk');
const _ = require('lodash');

const lib = require('./lib');

const CLOUDFORMATION = new AWS.CloudFormation();
const CLOUDFORMATION_ROLE_ARN = process.env.CLOUDFORMATION_ROLE_ARN;
const EMAIL_CUSTOM_RESOURCE_ARN = process.env.EMAIL_CUSTOM_RESOURCE_ARN;

async function createStack(userId, parameters) {
  let result

  const TemplateBody = lib.loadTemplateFile((parameters.filter(
    (parameter) => _.get(parameter, "ParameterKey", undefined) == "EbsVolumeId")).length > 0 ?
    "./templates/template-with-volume.yml" : "./templates/template.yml");

  result = await CLOUDFORMATION.createStack({
    StackName: `VisualCodeServer-${userId}`,
    DisableRollback: false,
    TemplateBody,
    Parameters: [...parameters, {
      "ParameterKey": "EmailSenderCustomResourceArn",
      "ParameterValue": EMAIL_CUSTOM_RESOURCE_ARN
    }],
    Capabilities: ["CAPABILITY_IAM", "CAPABILITY_NAMED_IAM", "CAPABILITY_AUTO_EXPAND"],
    RoleARN: CLOUDFORMATION_ROLE_ARN
  }).promise();

  return result
}

async function deleteStack(stackId) {
  let result

  result = await CLOUDFORMATION.createStack({
    StackName: stackId,
    RoleARN: CLOUDFORMATION_ROLE_ARN
  }).promise();

  return result
}

async function getStack(stackId) {
  let result

  try {
    result = _.get(await CLOUDFORMATION.describeStacks({
      StackName: stackId
    }).promise(), 'Stacks[0]', undefined)
  } catch (error) {
    console.error(error) 
  }

  return result
}

module.exports = {
  getStack,
  createStack,
  deleteStack,
}