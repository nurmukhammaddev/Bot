import asyncio

from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Text
from insta import instadownloader
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from tiktok import tiktok


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message:types.Message):
    link = message.text
    data = instadownloader(link=link)

    if data == "error":
        await message.answer("Nothing was found through this link. Chanel @the_best_python")
    else:
        if data['type'] =='image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] =='video':
            wait = await message.answer("Please wait... ⏳")
            await message.answer_video(video=data['media'], caption="Saved @saveinstikbot \nChanel @the_best_python")
            await wait.delete()
        elif data['type'] =='carousel':
            for i in data['media']:
                wait = await message.answer("Please wait... ⏳")
                await message.answer_document(document=i)
                await wait.delete()
                
        else:
            await message.answer("Nothing was found through this link. Chanel @the_best_python")




@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
async def test(message:types.Message):
    natija = tiktok(message.text)
    music = natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Download music", url ='{}'.
            format(music))]
        ]
    )
    await message.answer_video(natija['video'], reply_markup=btn, caption="Saved -> @saveinstikbot")


@dp.message_handler(Text(startswith='https://www.tiktok.com/'))
async def test(message:types.Message):
    natija = tiktok(message.text)
    music = natija['music']

    btn = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Download music", url ='{}'.
            format(music))]
        ]
    )
    wait = await message.answer("Please wait... ⏳")
    await message.answer_audio(natija['video'], reply_markup=btn)
    await wait.delete()

