def synchronize_databases(legacy_list, modern_set, blacklist):
    legacy = set(legacy_list)
    modern = set(modern_set)
    ban = set(blacklist)

    legacy_set = legacy - ban 



