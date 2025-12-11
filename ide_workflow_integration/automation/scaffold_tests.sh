#!/bin/bash
CLASS_NAME=$1
DIR_PATH=$2

if [[ "$DIR_PATH" == *"src/main/java"* ]]; then
    TEST_DIR=${DIR_PATH/src\/main\/java/src\/test\/java}
    TEST_FILE="${TEST_DIR}/${CLASS_NAME}Test.java"
    mkdir -p "$TEST_DIR"
    
    if [ ! -f "$TEST_FILE" ]; then
        echo "package $(basename $DIR_PATH);" > "$TEST_FILE"
        echo "@SpringBootTest class ${CLASS_NAME}Test {}" >> "$TEST_FILE"
    fi
fi
