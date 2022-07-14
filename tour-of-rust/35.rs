struct BagOfHolding<T> {
    item: Option<T>,
}

fn main() {
    let i32_bag = BagOfHolding::<i32> { item: None };
    if i32_bag.item.is_none() {
        println!("バッグには何もない!")
    } else {
        println!("バッグには何かある!")
    }

    let i32_bag = BagOfHolding::<i32> {item: Some(42) };
    if i32_bag.item.is_some() {
        println!("バッグにはなにかある!")
    } else {
        println!("バッグには何もない!")
    }

    match i32_bag.item {
        Some(v) => println!("バッグに {} を発見!", v),
        None => println!("何も見つからなかった")
    }
}
