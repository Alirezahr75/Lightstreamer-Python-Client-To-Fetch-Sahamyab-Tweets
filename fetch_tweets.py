from lightstreamer_client import *


def on_item_update(new_item):
	print(new_item)

def wait_for_input():
	input("{0:-^80}\n".format("HIT CR TO UNSUBSCRIBE AND DISCONNECT FROM LIGHTSTREAMER"))

sahamyab_client = {
	"lightstreamer_username": None,
	"lightstreamer_password": None,
	"lightstreamer_url": "https://push.sahamyab.com",
	"adapter_set": "STOCKLISTDEMO_REMOTE"
}

sahamyab_subscription = {
	"mode": "DISTINCT",
	"items": ["general ads"],
	"fields": ["id", "ads", "parentId", "parentSenderName", "parentSenderUsername", "parentContent", "parentSendTime", "retwitSenderName", "retwitSenderUsername", "retwitSendTime", "senderName", "senderUsername", "content", "sendTime", "likeCount", "commentCount", "retwitCount", "liked", "type", "senderProfileImage", "parentSenderProfileImage", "imageUid", "fileUid", "parentImageUid", "senderIsOfficial", "videoUid", "mediaContentType", "editable", "sendTimePersian", "status", "hasChart", "parentDeleted", "options", "finalPullDatePersian", "finalPullDate", "durationPerHour", "durationPerDay", "parentType", "parentDurationPerDay", "parentDurationPerHour", "parentOptions", "pullStatus", "parentPullStatus", "voteCount", "parentVoteCount"],
	"adapter": "QUOTE_ADAPTER"
}


lightstreamer_client = LightstreamerClient(**sahamyab_client)
lightstreamer_client.connect()

subscription = LightstreamerSubscription(**sahamyab_subscription)
subscription.addlistener(on_item_update)
lightstreamer_client.subscribe(subscription)

wait_for_input()
lightstreamer_client.unsubscribe(subscription)
lightstreamer_client.disconnect()
