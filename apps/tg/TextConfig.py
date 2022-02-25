
class Texts():
    welcomemes = 'Привет, {firstname}! Начнем...'
    comebackmes = 'Обязательно возвращайся!'
    errormes = 'Ой, что-то пошло не так. Попробуй еще раз.'
    successful_payment = "Ура! Платеж на сумму `{total_amount} {currency}` совершен успешно!" \
                         "Приятного пользования нашим сервисом!"
    sendinstuct = '📨Остаток сообщений: {mescount}\n\n💬Для создания рассылки:\n\n' \
                  '1. Пополняй баланс через ЮКасса и приобретай сообщения💳\n\n' \
                  '2. Добавляй ⚡️новую целевую аудиторию, выбирай\n' \
                  '👤существующую или используй 🔥нашу ЦА🔥 для максимального эффекта!\n\n' \
                  '3. Запускай✅'
    profiletext = 'Твой Ник: {username}\nТвоя команда: {team_occupied} из {team_volume}\n' \
        'Чаты для парсинга: {cells} из {cells_occupied}\n({chats})\n' \
                  'Рефералы: {refcount}\nСуб-рефералы: {subrefcount}\nКошелёк Голды: {balance}'
    abouttext = 'Тут что-то о нас вроде как, поэтому как бы да'
    supporttext = 'Ты можешь обратиться к нашему менеджеру напрямую'
    partertext = 'Приведено рефералов: {refcount}\nПривели твои рефералы: {subrefcount}\n' \
                 'Баланс: {balance}\nТвоя ссылка: {referal_link}\n\n'
    channel_invite = 'Для пользования функционалом бота ты должен\n\n ❌ Подписаться на канал\n\n'
    sub_decline = 'Не-а, ты еще не подписался)\n\n'
    refererr = 'Ты не можешь пригласить себя сам'
    keep_money = 'Тут должно лежать положение о выводе средств'
    homebutt = 'Домой'
    choose = 'Выберите предпочитаемый пакет:'
    bad_deep = 'У тебя битая ссылка, рефералка не зачтена'
    refer_dump = 'У тебя уже есть реферер'
    get_chat_member_err = 'Бот не состоит в группе, проверка не может быть пройдена.'


class Links():
    feedbacklink = 'https://t.me/+5nxj8AINWBtlMTUy'
    supportlink = 'http://t.me/TeleTargetSupportRobot'
    channel = None
    channel_id = '@wrldofbots'
    channel_url = 'https://t.me/wrldofbots'