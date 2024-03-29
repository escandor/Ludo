import pygame


BLACK = 0,0,0
tokenPoly = [[27.5, 30.5], [27.0, 30.5], [27.0, 26.5], [23.5, 14.5], [23.5, 14.5], [24.5, 13.5], [24.5, 13.0], [23.5, 12.0], [23.5, 12.0], [25.5, 7.0], [18.5, 0.0], [11.0, 7.0], [13.5, 12.0], [13.0, 12.0], [12.0, 13.0], [12.0, 13.5], [13.0, 14.5], [13.5, 14.5], [10.0, 26.5], [10.0, 30.5], [9.0, 30.5], [8.0, 31.5], [8.0, 34.0], [9.0, 35.0], [9.0, 35.0], [9.0, 37.0], [27.5, 37.0], [27.5, 35.0], [28.5, 34.0], [28.5, 31.5], [27.5, 30.5]]
class TokenCreate:
    def __init__(self, tokenNum,tokenColour, playerOwner, tokenLocation, baseCoord, tokenTilesPath, display = None):
        self.display = display
        self.tokenID = (tokenNum, tokenColour)
        self.playerOwner = playerOwner
        self.tokenLocation = tokenLocation
        # new
        self.xBaseCoord, self.yBaseCoord = baseCoord
        self.tokenTilesPath = tokenTilesPath
        self.currentTilePathPosition = 0

    def drawOtherPlayersTokens(self,otherPlayers,refresh):
        for player in otherPlayers:
            for token in player.tokensOnPath:
                new_translated_token_path = [[x + token.tokenLocation[0][0], token.tokenLocation[1][0] +y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,player.colour,new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path,1)
            # when other player is doing their turn all of the other player's tokens don't move
            for token in player.tokensOnBase:
                new_translated_token_path = [[x + token.xBaseCoord, token.yBaseCoord+y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,player.colour,new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path,1)
            for token in player.tokensOnHome:
                new_translated_token_path = [[x + token.tokenLocation[0][0], token.tokenLocation[1][0] +y] for [x, y] in tokenPoly]
                pygame.draw.polygon(refresh.gameDisplay,player.colour,new_translated_token_path)
                pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path,1)
            
    def tokenNewTile(self,moveBy):
        return self.tokenTilesPath[self.currentTilePathPosition+moveBy][0]

    def moveOneToken(self,refresh,colour,path):
        pygame.draw.polygon(refresh.gameDisplay,colour,path)
        pygame.draw.polygon(refresh.gameDisplay, BLACK, path,1)

    def setCurrentTilePathPosition(self,moveBy):
        if moveBy != 0:
            self.currentTilePathPosition += moveBy
        else:
            self.currentTilePathPosition = moveBy

    def setPlayerOwner(self,player):
        self.playerOwner = player
    
    def setTokenLocation(self,newtokenLocation):
        self.tokenLocation = newtokenLocation

    def getLocation(self):
        return self.tokenLocation

    def setPlayerOwner(self, player):
        self.playerOwner = player

    def setLocation(self):
        pass

    def drawToken(self,refresh):
        new_translated_token_path = [[x + self.tokenLocation[0][0], self.tokenLocation[1][0] + y] for [x, y] in tokenPoly]
        pygame.draw.polygon(refresh.gameDisplay,self.tokenID[1],new_translated_token_path)
        pygame.draw.polygon(refresh.gameDisplay, BLACK, new_translated_token_path,1)