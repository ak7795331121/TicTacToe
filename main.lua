
local turn = 0

local xpos = -150
local ypos = -150

function com()
	turn = 0
end

function love.load( ) 
	love.graphics.setFont(love.graphics.newFont(16))
end

function love.update(dt)
	if turn == 0 then
		if love.keyboard.isDown("1") then
			xpos = 300
			ypos = 130
			turn = 1 
			
		end
		if love.keyboard.isDown("2") then
			xpos = 400
			ypos = 130
		end
		if love.keyboard.isDown("3") then
			xpos = 500
			ypos = 130
		end
		if love.keyboard.isDown("4") then
			xpos = 300
			ypos = 230
		end
		if love.keyboard.isDown("5") then
			xpos = 400
			ypos = 230
		end
		if love.keyboard.isDown("6") then
			xpos = 500
			ypos = 230
		end
		if love.keyboard.isDown("7") then
			xpos = 300
			ypos = 330
		end
		if love.keyboard.isDown("8") then
			xpos = 400
			ypos = 330
		end
		if love.keyboard.isDown("9") then
			xpos = 500
			ypos = 330
		end
	end
end

function love.draw()
	-- Draw Horizontal Lines
	love.graphics.line(270,200,570,200)
	love.graphics.line(270,300,570,300)
	-- Draw Vertical Lines
	love.graphics.line(370,100,370,400)
	love.graphics.line(470,100,470,400)
	if turn == 1 then
		love.graphics.print("COMPUTER's TURN Please Wait.......",0,0)
		com()
	else
		love.graphics.print("YOUR TURN Please Press the position you want to place.....",0,0)
	end
	love.graphics.print(1,350,180)
	love.graphics.print(2,450,180)
	love.graphics.print(3,550,180)
	love.graphics.print(4,350,280)
	love.graphics.print(5,450,280)
	love.graphics.print(6,550,280)
	love.graphics.print(7,350,380)
	love.graphics.print(8,450,380)
	love.graphics.print(9,550,380)
-- Printing X or O 
	love.graphics.setFont(love.graphics.newFont(36))
	love.graphics.print('X',xpos,ypos)
	love.graphics.setFont(love.graphics.newFont(16))


end

