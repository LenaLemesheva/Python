
import enter as en
import logger
import view


def start():
    button = view.choice()
    if button == 1:
        print('Вносите абонент')
        contact = en.enter()
        logger.log_to_file(contact)
        start()
    if button == 2:
        print('Работа окончена')
        exit