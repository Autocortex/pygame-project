def build_profile(first, last, **user_info):
	"""Строит словарь с информацией о пользователе."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info