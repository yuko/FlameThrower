BEGIN;
CREATE TABLE "basil_account" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL);
CREATE TABLE "basil_accounttype" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "account_type" varchar(200) NOT NULL);
CREATE TABLE "basil_account__new" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(200) NOT NULL, "account_type_id" integer NOT NULL REFERENCES "basil_accounttype" ("id"));
INSERT INTO "basil_account__new" ("account_type_id", "id", "name") SELECT NULL, "id", "name" FROM "basil_account";
DROP TABLE "basil_account";
ALTER TABLE "basil_account__new" RENAME TO "basil_account";
CREATE INDEX "basil_account_d18f477c" ON "basil_account" ("account_type_id");

COMMIT;
