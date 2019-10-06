const api = require('./api')

exports.handler = async (event, context) => {
  return api.run(event, context)
}