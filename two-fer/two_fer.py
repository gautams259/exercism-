def two_fer(name=None):
    if name:
        return "One for {}, one for me.".format(name)
    else:
        return "One for you, one for me."


if __name__ == '__main__':
    print two_fer('deepak')
