-- Nova Studio Luau Examples

local Examples = {}

Examples.CreatePart = function()
	local part = Instance.new("Part")
	part.Size = Vector3.new(4,4,4)
	part.Position = Vector3.new(0,5,0)
	part.Anchored = true
	part.Parent = workspace
	
	return part
end


Examples.ChangeColor = function(part, color)
	part.Color = color
end


return Examples
