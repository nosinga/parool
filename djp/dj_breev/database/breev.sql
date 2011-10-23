-- python manage.py sql breev         >> database/breev.sql 
BEGIN;
CREATE TABLE "breev_aukartikelrankvw" (
    "id" serial NOT NULL PRIMARY KEY,
    "artikel_id" integer NOT NULL,
    "artikel_titel" varchar(200) NOT NULL,
    "krant" text NOT NULL,
    "cat_id" integer NOT NULL,
    "cat_volgorde" integer NOT NULL,
    "categorie" varchar(200) NOT NULL,
    "pubdate" timestamp with time zone NOT NULL,
    "pubdate_yyyymmdd" text NOT NULL,
    "krant_weight" numeric(10, 6) NOT NULL,
    "calculated_weight" numeric(10, 6) NOT NULL,
    "cloud_weight" numeric(10, 6) NOT NULL,
    "total_weight" numeric(10, 6) NOT NULL,
    "rank" numeric(10, 6) NOT NULL
)
;
CREATE TABLE "auk_artikel" (
    "id" serial NOT NULL PRIMARY KEY,
    "uniek" varchar(200) NOT NULL UNIQUE,
    "titel" varchar(200) NOT NULL,
    "pubdate" timestamp with time zone NOT NULL,
    "rssfeeddescription" varchar(4000) NOT NULL,
    "url" varchar(1000) NOT NULL,
    "body" varchar(64000) NOT NULL,
    "body_clean" varchar(64000) NOT NULL
)
;
CREATE TABLE "auk_krant" (
    "id" serial NOT NULL PRIMARY KEY,
    "naam" varchar(100) NOT NULL UNIQUE,
    "url" varchar(1000) NOT NULL
)
;
CREATE TABLE "auk_rubriek" (
    "id" serial NOT NULL PRIMARY KEY,
    "krt_id" integer NOT NULL REFERENCES "auk_krant" ("id") DEFERRABLE INITIALLY DEFERRED,
    "naam" varchar(100) NOT NULL,
    "url" varchar(1000) NOT NULL UNIQUE,
    "actief" varchar(1) NOT NULL
)
;
CREATE TABLE "auk_categorie" (
    "id" serial NOT NULL PRIMARY KEY,
    "volgorde" integer NOT NULL,
    "naam" varchar(100) NOT NULL UNIQUE,
    "cloud" varchar(4000),
    "cloud_factor" numeric(4, 2) NOT NULL,
    "aging_factor" numeric(4, 2) NOT NULL
)
;
CREATE TABLE "auk_gebruiker_categorie" (
    "id" serial NOT NULL PRIMARY KEY,
    "usr_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "cat_id" integer NOT NULL REFERENCES "auk_categorie" ("id") DEFERRABLE INITIALLY DEFERRED,
    "volgorde" integer NOT NULL,
    "aantal_artikelen" integer NOT NULL,
    UNIQUE ("usr_id", "cat_id")
)
;
CREATE TABLE "auk_rubriek_categorie" (
    "id" serial NOT NULL PRIMARY KEY,
    "rbk_id" integer NOT NULL REFERENCES "auk_rubriek" ("id") DEFERRABLE INITIALLY DEFERRED,
    "cat_id" integer NOT NULL REFERENCES "auk_categorie" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("rbk_id", "cat_id")
)
;
CREATE TABLE "auk_artikel_categorie" (
    "id" serial NOT NULL PRIMARY KEY,
    "art_id" integer NOT NULL REFERENCES "auk_artikel" ("id") DEFERRABLE INITIALLY DEFERRED,
    "cat_id" integer NOT NULL REFERENCES "auk_categorie" ("id") DEFERRABLE INITIALLY DEFERRED,
    "krant_weight" double precision,
    "calculated_weight" double precision,
    "cloud_weight" double precision,
    "total_weight" double precision,
    "rank" integer,
    UNIQUE ("art_id", "cat_id")
)
;
CREATE TABLE "auk_artikel_publicatie" (
    "id" serial NOT NULL PRIMARY KEY,
    "art_id" integer NOT NULL REFERENCES "auk_artikel" ("id") DEFERRABLE INITIALLY DEFERRED,
    "rbk_id" integer NOT NULL REFERENCES "auk_rubriek" ("id") DEFERRABLE INITIALLY DEFERRED,
    UNIQUE ("art_id", "rbk_id")
)
;
CREATE TABLE "sar_ignorewordlist" (
    "id" serial NOT NULL PRIMARY KEY,
    "word" varchar(4000) NOT NULL
)
;
CREATE TABLE "sar_wordlist" (
    "id" serial NOT NULL PRIMARY KEY,
    "word" varchar(4000) NOT NULL UNIQUE
)
;
CREATE TABLE "sar_wordlocation" (
    "id" serial NOT NULL PRIMARY KEY,
    "art_id" integer NOT NULL REFERENCES "auk_artikel" ("id") DEFERRABLE INITIALLY DEFERRED,
    "wrd_id" integer NOT NULL REFERENCES "sar_wordlist" ("id") DEFERRABLE INITIALLY DEFERRED,
    "location" integer NOT NULL,
    UNIQUE ("art_id", "wrd_id", "location")
)
;
CREATE TABLE "breev_logaction" (
    "id" serial NOT NULL PRIMARY KEY,
    "usr_id" integer REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "art_id" integer REFERENCES "auk_artikel" ("id") DEFERRABLE INITIALLY DEFERRED,
    "session_key" varchar(40) NOT NULL,
    "first_action_time" timestamp with time zone NOT NULL,
    "last_action_time" timestamp with time zone NOT NULL,
    "action" varchar(100) NOT NULL,
    "spent_time" integer NOT NULL
)
;
CREATE TABLE "breev_vote" (
    "id" serial NOT NULL PRIMARY KEY,
    "usr_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED,
    "art_id" integer NOT NULL REFERENCES "auk_artikel" ("id") DEFERRABLE INITIALLY DEFERRED,
    "score" integer NOT NULL
)
;
COMMIT;
