# coding=utf-8
from collections import defaultdict


class Twitter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.friends = defaultdict(set)
        self.tweet = defaultdict(list)
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: void
        """
        self.follow(userId, userId)
        self.tweet[userId].append((self .time, tweetId,))
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        res = []
        for friend in self.friends[userId] :
            res.extend(self.tweet[friend])
        res = sorted(res,reverse=True)[ :10]
        res = [t[1] for t in res]
        return res

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId is not None and followeeId is not None:
            self.friends[followerId].add (followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: void
        """
        if followerId is not None and followeeId is not None and followeeId != followerId:

