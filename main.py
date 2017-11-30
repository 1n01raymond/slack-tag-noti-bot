@import time
import  random
from slackclient import SlackClient

SLACK_BOT_TOKEN = 'xoxb-279497069155-Anbld4kuADulu6sAtAk8Jihg'
BOT_NAME = 'jira-tag-noti-bot'
READ_DELAY = 1

slack_client = SlackClient(SLACK_BOT_TOKEN)


def parse(slack_rtm_output):
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and '@' in output['text']:
                return True, output['channel'], filter(lambda x:'@'in x, output['text'].split(' '))

    return False, None


def handle(channel, list):
	for item in list:
		slack_client.api_call("chat.postMessage", link_names=1, channel=channel, text=item, as_user=True)


if __name__ == "__main__":
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            has_sora, channel, list = parse(slack_client.rtm_read())
            if has_sora:
                handle(channel, list)

            time.sleep(READ_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
