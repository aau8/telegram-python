import sqlite3

DB_PATH = './history.db'

def write_message_to_db(msg):
	db = sqlite3.connect(DB_PATH)

	try:
		with db:
			cursor = db.cursor()
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS history(
					text TEXT,
					chat_id INT,
					user_id INT
				)
			""")
			db.commit()

			cursor.execute("INSERT INTO history VALUES(?, ?, ?)", (msg.text, msg.chat.id, msg.from_user.id))

	finally:
		db.close()


def write_chat_to_db(msg):
	db = sqlite3.connect(DB_PATH)

	try:
		with db:
			cursor = db.cursor()

			cursor.execute("""
				CREATE TABLE IF NOT EXISTS chats(
					id INT,
					title TEXT,
					username TEXT,
					type TEXT
				);
			""")
			db.commit()


			chat = cursor.execute("SELECT * FROM chats WHERE id=?", (int(msg.chat.id),)).fetchone()

			# Если чата нет в БД, то он добавится
			if chat is None:
				cursor.execute("INSERT INTO chats VALUES(?, ?, ?, ?)", (int(msg.chat.id), msg.chat.title, msg.chat.username, msg.chat.type))

			# Если у чата изменился username, запись обновится
			elif chat[2] != msg.chat.username:
				cursor.execute("UPDATE chats SET username=? WHERE id=?", (msg.chat.username, int(msg.chat.id)))


	finally:
		db.close()


def check_pass_to_db(msg):
	db = sqlite3.connect(DB_PATH)

	try:
		with db:
			cursor = db.cursor()
			cursor.execute("SELECT value FROM config WHERE name='password'")

			return cursor.fetchone()[0]

	finally:
		db.close()


def add_user_to_blacklist(msg):
	db = sqlite3.connect(DB_PATH)

	try:
		with db:
			cursor = db.cursor()

			cursor.execute("""
				CREATE TABLE IF NOT EXISTS blacklist(
					id INT,
					username TEXT,
					fname TEXT,
					lname TEXT
				);
			""")
			db.commit()

			cursor.execute("INSERT INTO blacklist VALUES(?, ?, ?, ?)", (int(msg.from_user.id), msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name))
			print(f"Пользователь {msg.from_user.first_name} (https://t.me/{msg.from_user.username}) добавлен в черный список")

	finally:
		db.close()


def check_user_to_blacklist(msg):
	db = sqlite3.connect(DB_PATH)

	try:
		with db:
			cursor = db.cursor()

			cursor.execute("""
				CREATE TABLE IF NOT EXISTS blacklist(
					id INT,
					username TEXT,
					fname TEXT,
					lname TEXT
				);
			""")
			db.commit()

			cursor.execute("SELECT * FROM blacklist WHERE id=? OR username=?", (int(msg.from_user.id), msg.from_user.username))

			return cursor.fetchone()

	finally:
		db.close()