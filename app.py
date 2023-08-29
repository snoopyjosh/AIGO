from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError

from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi(
    "15DDILqV4rxCdYeQEpkMK30OeRiXRBC3M2mlGUz7/ljzcLP2qcsSi6gYrpA/IfQdl5tzqIkuNnhilaMzl4m4trIBrXnGkRtJLjXkXROWJXqwkEKsZH6Qb7xUUQCvXewih2II0E4G2r8yrPt8P8tKZwdB04t89/1O/w1cDnyilFU="
)
handler = WebhookHandler("549c652964c34ccf90318421ef371d04")


def about_us_event(event):
    emoji = [
        {"index": 0, "productId": "5ac21184040ab15980c9b43a", "emojiId": "225"},
        {"index": 17, "productId": "5ac21184040ab15980c9b43a", "emojiId": "225"},
    ]

    text_message = TextSendMessage(
        text="""$ Master RenderP $
Hello! 您好，歡迎您成為 Master RenderP 的好友！

我是Master 支付小幫手 

-這裡有商城，還可以購物喔~
-直接點選下方【圖中】選單功能

-期待您的光臨！""",
        emojis=emoji,
    )

    sticker_message = StickerSendMessage(package_id="8522", sticker_id="16581271")
    line_bot_api.reply_message(event.reply_token, [text_message, sticker_message])


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # event有什麼資料？詳見補充

    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text="Hi! Welcome to LSTORE.")
    )


if __name__ == "__main__":
    app.run()
