import random
from aiogram import F, Router
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from src.get_city import *

router = Router()


class PlayState(StatesGroup):
    playing = State()
    class_object = None
    word = None


@router.message(Command('start', 'stop'))
async def start_handler(message: Message):
    user_id = message.from_user.id
    user_full_name = message.from_user.full_name
    user_name = message.from_user.first_name
    catalog = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Города Европы', callback_data="0")],
                                                    [InlineKeyboardButton(text='Города Азии', callback_data="1")],
                                                    [InlineKeyboardButton(text='Города Африки', callback_data="2")],
                                                    [InlineKeyboardButton(text='Города Северной Америки',
                                                                          callback_data="3")],
                                                    [InlineKeyboardButton(text='Города Южной Америки',
                                                                          callback_data="4")],
                                                    [InlineKeyboardButton(text='Города Океании', callback_data="5")],
                                                    [InlineKeyboardButton(text='Правила игры', callback_data='help')]])
    await message.answer(
        text=f'Привет, {user_full_name}! Я бот для игры в города. Поиграем?:) Выбери категорию городов из списка ниже',
        reply_markup=catalog)


@router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(MESSAGE_HELP)


@router.callback_query(F.data == 'help')
async def callback_handler_help(callback: CallbackQuery):
    await callback.message.answer(MESSAGE_HELP)


@router.callback_query(F.data == "0")
async def callback_handler_0(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 0
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.callback_query(F.data == "1")
async def callback_handler_1(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 1
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.callback_query(F.data == "2")
async def callback_handler_2(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 2
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.callback_query(F.data == "3")
async def callback_handler_3(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 3
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.callback_query(F.data == "4")
async def callback_handler_4(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 4
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.callback_query(F.data == "5")
async def callback_handler_5(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 5
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.callback_query(F.data == "6")
async def callback_handler_6(callback: CallbackQuery, state: FSMContext):
    await state.set_state(PlayState.playing)
    PlayState.word = 6
    await callback.message.answer(f'Вы выбрали категорию: {list_categories[PlayState.word]}')
    await callback.message.answer(
        f'Чтобы игра была интересной, мне нужно знать много городов. Я использую большую базу данных, нужно чуть-чуть подождать, пока она загрузится :)')
    PlayState.class_object = GetCity(all_continents[PlayState.word])
    cur_city = random.choice(PlayState.class_object.all_cities["А"])
    await callback.message.answer(cur_city)
    PlayState.class_object.used_cities.append(cur_city)


@router.message(PlayState.playing)
async def callback_handler_play(message: Message, state: FSMContext):
    cur_city = message.text.capitalize()
    if cur_city[0].lower() != performing_word(PlayState.class_object.used_cities[-1])[-1].lower():
        await message.answer("Слово начинается не на ту же букву, на которую закончилось предыдущее")
    else:
        if cur_city not in PlayState.class_object.all_cities[cur_city[0]]:
            await message.answer("Я не знаю такого города :(")
        else:
            if cur_city in PlayState.class_object.used_cities:
                await message.answer("Такое слово уже было")
            else:
                PlayState.class_object.used_cities.append(cur_city)
                cur_city = random.choice(PlayState.class_object.all_cities[message.text[-1].upper()])
                PlayState.class_object.used_cities.append(cur_city)
                await message.answer(cur_city)
