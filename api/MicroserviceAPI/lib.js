const fs = require("fs");
const path = require("path");

module.exports = {
    loadTemplateFile: function (templateName) {
        const fileName = `${templateName}`
        let resolved
        if (process.env.LAMBDA_TASK_ROOT) {
            resolved = path.resolve(process.env.LAMBDA_TASK_ROOT, fileName)
        } else {
            resolved = path.resolve(__dirname, fileName)
        }
        console.log(`Loading template at: ${resolved}`)
        try {
            const data = fs.readFileSync(resolved, 'utf8')
            return data
        } catch (error) {
            const message = `Could not load template at: ${resolved}, error: ${JSON.stringify(error, null, 2)}`
            console.error(message)
            throw new Error(message)
        }
    },
};