class MegaGreeter
  attr_accessor :names

  def initialize(names = "World")
    @names = names
  end

  def say_hi
    if @names.nil?
      puts "..."
    elsif @names.respond_to?("each")
      @names.each do |name|
        puts "Hello #{name}!"
      end
    else
      puts "Hello #{@names}!"
    end
  end

  def say_bye
    if @names.nil?
      puts "...."
    elsif @names.respond_to?("join")
      puts "Goodbye #{@names.join(", ")}, Come back soon!"
    else
      puts "Goodbye #{@names}, Come back soon!"
    end
  end
end

if __FILE__ == $0
  puts "[+] empty:"
  mg = MegaGreeter.new
  mg.say_hi
  mg.say_bye

  puts "\n[+] Zeka"
  mg.names = "Zeka"
  mg.say_hi
  mg.say_bye

  puts "\n[+] list of name"
  mg.names = ["piko", "tako", "poyo", "uwu"]
  mg.say_hi
  mg.say_bye

  puts "\n[+] nil"
  mg.names = nil
  mg.say_hi
  mg.say_bye
end
