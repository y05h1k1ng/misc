# https://keens.github.io/blog/2017/10/17/fun_ikideshieruwotsukatteiruninnotamenoshierunyuumon/

# 代入の=の前後に空白を入れるとエラー
version=1.0
echo /path/to/lang/$version/bin/lang-$version

# [0-9a-zA-Z_]+ が変数名
# $version_dateが変数だと認識されてる
echo lang_$version_date
# ${変数}で区切るとOK
echo lang_${version}_date

# 環境変数
export hoge
export hoge=fuga

# 文字列
hoge=world
# "文字列"は変数とかを展開してくれる
echo "hello\n$hoge"
# => hello
# => world
# '文字列'は変数の展開がされない
echo 'hello\n$hoge'
# => hello
# => $hoge
# 'のエスケープ
echo "I'm good"
# '文字列'でどうしても使いたかったら、文字列を一旦'I'で区切りそのまま\'で続ける
# スペースさえ空いていなければ、一つの文字列として認識される仕様
echo 'I'\''m good'

tako=yaki
cat <<EOF
This is $hoge
That is $tako
EOF
# 'EOF'にすると変数の展開がされない
cat <<'EOF'
This is $hoge
That is $tako
EOF
# パイプ
cat <<EOF |tr a-z A-Z
hello
EOF

# 結果を変数に入れたいときとか
# バッククォート記法
ok=`echo ok`
echo $ok
# バックスラッシュでさらにネスト
echo `echo \`echo ok\``
# $()記法
# 実はPOSIX基準ではない（が、ほとんどのシェルで使えるので気にしなくてもいい？）
echo $(echo ok)
echo $(echo $(echo ok))

# if文
if grep hoge /etc/passwd > /dev/null 2>&1; then
    # exit status が0
    echo "Hello, hoge"
else
    # それ以外
    echo "hoge..."
fi

# 論理演算
echo 1 && echo 2 | cat
# => 1
# => 2
echo 1 || echo 2 | cat
# => 1
! echo 1 && ! echo 2 | cat
# => 1
! echo 1 || ! echo 2 | cat
# => 1
# => 2

# test文
#[]で書ける
# [ 1 = 1]だと最後の引数が1]になるのでエラー、空白をつける
n=1
if [ "$n" -lt 0 ]; then # n < 0
    echo "n is negative"
elif [ 0 -le "$n" ] && [ "$n" -lt 10 ]; then # (0 <= n) && (n < 10)
    echo "n is small"
else
    echo "n is big"
fi

echo $((1+1))
expr 1 + 1
