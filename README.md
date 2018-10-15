# slash-command-lambda
Execute Slack's slash command from AWS Lambda.

## Usage

### AWS Setting
- Code entry type : Upload a .zip file  
  - upload `slash-command-lambda/ambda.zip`
  - set handler `slack_slash_command.lambda_handler`
- set Environment variables
   - `API_TOKEN`
      - https://api.slack.com/custom-integrations/legacy-tokens
   - `CHANNEL`
      - This should be an ID, such as `C8UJ12P4P`.
   - `COMMAND`
      - ex. `/shurg`
   - `TEXT (Optional)`
      - ex. `*slash-command-lambda*`

### Result
<img width="521" alt="result" src="https://user-images.githubusercontent.com/4005383/46964817-11874a00-d0e4-11e8-9178-cdb9e857574d.png">

## Custom build
- add package
  - `pip install <<package>> -t .`
- build zip
  - `zip -r <<filename>> *`
