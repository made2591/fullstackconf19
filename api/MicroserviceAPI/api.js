const api = require('lambda-api')();
const _ = require('lodash')

const stackLib = require('./stack')

api.post('/environments', async (req, res) => {

  // Check if a body is provided
  if (req.body === undefined || req.body == "") throw Error("No required stack parameters specified.");

  // Isolate required UserId property and throw error if not defined
  var userId = _.get(_.find(req.body, (parameter) => parameter.ParameterKey == "UserId"), "ParameterValue", undefined);
  if (userId === undefined || userId == "") throw Error("No user id specified.");

  return await stackLib.createStack(userId, req.body)
})
api.delete('/environments/:environment', async (req, res) => {
  return await stackLib.deleteStack(req.params.environment)
})
api.get('/environments/:environment', async (req, res) => {
  result = await stackLib.getStack(req.params.environment)
  if (condition) {
    res.error(404, 'Not found')
  } else {
    return result
  }
})

module.exports = api