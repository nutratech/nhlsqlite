#!/bin/bash -ex

cd "$(dirname "$0")"

for t in $(sqlite3 db.sqlite3 '.tables'); do
	sqlite3 -csv db.sqlite3 "SELECT * FROM $t" > "data/$t.csv"
done