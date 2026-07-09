from community_postgis.native_validator import security_check


# ── Blocked ───────────────────────────────────────────────────────────────────

def test_drop_is_blocked():
    assert len(security_check("DROP TABLE locations")) > 0


def test_truncate_is_blocked():
    assert len(security_check("TRUNCATE locations")) > 0


def test_delete_is_blocked():
    assert len(security_check("DELETE FROM locations")) > 0


def test_insert_is_blocked():
    assert len(security_check("INSERT INTO locations VALUES (1)")) > 0


def test_update_is_blocked():
    assert len(security_check("UPDATE locations SET geom = NULL")) > 0


def test_alter_is_blocked():
    assert len(security_check("ALTER TABLE locations ADD COLUMN x INT")) > 0


# ── Allowed ───────────────────────────────────────────────────────────────────

def test_st_within_select_is_allowed():
    assert security_check("SELECT * FROM locations WHERE ST_Within(geom, %s)") == []


def test_st_intersects_select_is_allowed():
    assert security_check("SELECT * FROM locations WHERE ST_Intersects(geom, %s)") == []


def test_st_dwithin_select_is_allowed():
    assert security_check("SELECT * FROM locations WHERE ST_DWithin(geom, %s, %s)") == []


# ── Case insensitive ──────────────────────────────────────────────────────────

def test_drop_lowercase_is_blocked():
    assert len(security_check("drop table locations")) > 0


def test_truncate_mixed_case_is_blocked():
    assert len(security_check("Truncate locations")) > 0
