function CampaignCard({
  campaign
}) {

  if (!campaign)
    return null;

  return (

    <div className="bg-white rounded-3xl p-8 shadow-sm border border-gray-100 mt-5">

      {/* Header */}
      <div className="flex items-center justify-between">

        <h3 className="font-bold text-2xl text-slate-800">
          Generated Campaign
        </h3>

        <span className="bg-green-100 text-green-700 px-4 py-2 rounded-full text-sm font-semibold">
          AI Generated
        </span>

      </div>

      {/* Channel */}
      <div className="mt-6">

        <p className="text-gray-500 text-sm">
          Recommended Channel
        </p>

        <h2 className="text-2xl font-bold text-indigo-600 mt-1">
          {
            campaign.recommended_channel
          }
        </h2>

      </div>

      {/* Reason */}
      <div className="mt-5">

        <p className="text-gray-500 text-sm">
          Why this channel?
        </p>

        <p className="text-slate-700 mt-1">
          {
            campaign.reason
          }
        </p>

      </div>

      {/* Campaign Message */}
      <div className="mt-6">

        <p className="text-gray-500 text-sm mb-2">
          Personalized Campaign Message
        </p>

        <div className="bg-slate-100 border border-slate-200 p-5 rounded-2xl text-slate-800 leading-relaxed">
          {
            campaign.campaign_message
          }
        </div>

      </div>

      {/* AI Insights */}
      <div className="mt-8 bg-gradient-to-r from-indigo-50 to-purple-50 border border-indigo-100 rounded-3xl p-6">

        <h3 className="font-bold text-xl text-slate-800 mb-4">
          AI Insights
        </h3>

        <div className="grid md:grid-cols-2 gap-5">

          <div className="bg-white rounded-2xl p-4 shadow-sm">

            <p className="text-sm text-gray-500">
              Best Audience
            </p>

            <h4 className="font-bold text-lg mt-1">
              Dormant Premium Shoppers
            </h4>

          </div>

          <div className="bg-white rounded-2xl p-4 shadow-sm">

            <p className="text-sm text-gray-500">
              Predicted Open Rate
            </p>

            <h4 className="font-bold text-lg mt-1 text-green-600">
              72%
            </h4>

          </div>

          <div className="bg-white rounded-2xl p-4 shadow-sm">

            <p className="text-sm text-gray-500">
              Recommended Send Time
            </p>

            <h4 className="font-bold text-lg mt-1">
              7 PM – 9 PM
            </h4>

          </div>

          <div className="bg-white rounded-2xl p-4 shadow-sm">

            <p className="text-sm text-gray-500">
              AI Recommendation
            </p>

            <h4 className="font-bold text-lg mt-1 text-purple-600">
              High Conversion Potential
            </h4>

          </div>

        </div>

        <div className="bg-white rounded-2xl p-5 mt-5 shadow-sm">

          <p className="text-gray-500 text-sm">
            Why this recommendation?
          </p>

          <p className="text-slate-700 mt-2 leading-relaxed">
            Premium dormant shoppers generally respond
            better to personalized WhatsApp offers and
            limited-time discounts during evening hours.
            AI predicts stronger re-engagement probability
            with incentive-based messaging.
          </p>

        </div>

      </div>

    </div>
  );
}

export default CampaignCard;