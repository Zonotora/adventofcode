lines = File.readlines("../input/01").map(&:to_i)

# part 1
puts lines.map { |l| l / 3 - 2}.sum

# part 2
def calc(fuel)
    mass = fuel / 3 - 2
    if  mass < 0
        return 0
    end
    return mass + calc(mass)
end

puts lines.map {|l| calc l}.sum