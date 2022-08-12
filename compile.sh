BASE_DIR="$PWD"
FLAG="$1"

compile_java_files() {
    DIR="$1"
    cd "$BASE_DIR/$DIR"
        for file in *
    do
        str="$file"
        len=${#str}
        end=$(($len-4));
        ext=$( echo "$file" |cut -c$end-$len )
        if [[ "$ext" == ".java" ]]
        then
            javac "./$file" 
        fi
    done
    clear
    echo "Java Files compiled in $DIR."
    cd "$BASE_DIR"
}

delete_java_classes() {
     DIR="$1"
    cd "$BASE_DIR/$DIR/"
        for file in *
    do
        str="$file"
        len=${#str}
        end=$(($len-5));
        ext=$( echo "$file" |cut -c"$end"-"$len" )
        if [[ "$ext" == ".class" ]]
        then
            rm "./$file" 
        fi
    done
    cd "$BASE_DIR"   
}

if [[ "$FLAG" == "binarytree" ]]
then
    compile_java_files binarytrees
fi

cd "$BASE_DIR"
javac ./Main.java
java Main "$FLAG"

delete_java_classes binarytrees
delete_java_classes